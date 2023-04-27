use master
go

set nocount on
go


select 'Free Space Before'
exec xp_fixeddrives
go


--gather data files to shrink

drop table if exists #data_files_to_shrink
go

create table #data_files_to_shrink
 ( id int identity,
   dbname varchar(100),
   filename varchar(100),
   size_before_kb bigint,
   size_after_kb bigint)
go

declare @db varchar(100)
declare @sql nvarchar(4000)

select @db = min(dbname) from zeyt..tblProgramDb

while @db is not null
begin
    set @sql = 'insert into #data_files_to_shrink (dbname, filename, size_before_kb)' +
               'select ''' + @db + ''', name, size * 8 as size_before_kb ' +
               ' from ' + @db + '.sys.database_files ' +
               ' where type_desc = ''LOG'' '

    --print @sql
    exec sp_executesql @sql

    select @db = min(dbname) from zeyt..tblProgramDB where dbname > @db
end
go


-- shrink data files
use master
go

declare @id int
declare @db varchar(100)
declare @filename varchar(100)
declare @sql nvarchar(4000)

select @id = min(id) from #data_files_to_shrink

while @id is not null
begin
  
  select @db = dbname, @filename = filename from #data_files_to_shrink where id = @id
  set @sql = 'use ' + @db +'; ' +
             'dbcc shrinkfile('''+@filename+''', 5) WITH NO_INFOMSGS; ' +
             ' update #data_files_to_shrink ' +
             ' set size_after_kb = (select size * 8 from ' + @db + '.sys.database_files where name = ''' + @filename + ''') ' +
             ' where id = ' + cast(@id as varchar) + ' '
             
  print @sql
  exec sp_executesql @sql

  select @id = min(id) from #data_files_to_shrink where id > @id

end  
go

select 'Free Space After'
exec xp_fixeddrives
go


select *, size_before_kb - size_after_kb as reclaimed_kb
from #data_files_to_shrink
go

-- drop table if exists #data_files_to_shrink
-- go
