# Exiftool

## If CreateDate tag is not present, try using DateTimeOriginal or FileModifyDate instead.

```
exiftool -s -G -api largefilesupport=1 
```

## rename

```
exiftool -r -overwrite_original -api largefilesupport=1 -d %Y/%m/%Y%m%d_%H%M%S%%-c.%%le "-FileName<CreateDate" .
exiftool -r -overwrite_original -api largefilesupport=1 -d %Y/%m/%Y%m%d_%H%M%S "-FileName<${FileCreateDate}.%e" .

exiftool -r -overwrite_original -api largefilesupport=1 "-FileName<${OrgSmpteMxfPackageMaterialPackagename}.%le"
```

## move to folder

```
exiftool -api largefilesupport=1 "-Directory<CreateDate" -d ./%Y/%m/%d -r .
exiftool -api largefilesupport=1 "-Directory<FileModifyDate" -d %Y/%m -r .
```

## ComPanasonicProfessionalpluginP2ClipmetadataShootStartdate
## ComPanasonicProfessionalpluginP2ClipmetadataShootEnddate

```
exiftool -progress -overwrite_original -api largefilesupport=1 "-AllDates<ComPanasonicProfessionalpluginP2ClipmetadataShootStartdate" -r .
```

## Set specific Date

```
exiftool -progress -overwrite_original -api largefilesupport=1 "-DateTimeOriginal=2015:01:10 13:15:06" .
```

## Timeshift Photos by One Year

```
exiftool -progress -overwrite_original -api largefilesupport=1 "-AllDates-=0:0:0 1" .

exiftool -progress -overwrite_original -api largefilesupport=1 "-FileCreateDate<CreateDate" "-FileModifyDate<CreateDate" "-TrackCreateDate<CreateDate"  "-TrackModifyDate<CreateDate" "-MediaCreateDate<CreateDate" "-MediaModifyDate<CreateDate" "-ModifyDate<CreateDate" "-AllDates<CreateDate" .

exiftool -progress -overwrite_original -api largefilesupport=1 -"AllDates<FileModifyDate" .

exiftool -progress -overwrite_original -api largefilesupport=1 "-ComPanasonicProfessionalpluginP2ClipmetadataShootStartdate<CreateDate" .
```
## To write one output file for all source files in each directory:

```
exiftool -progress -api largefilesupport=1 -FileName -CreateDate -ModifyDate -FileCreateDate -FileModifyDate -TrackCreateDate -TrackModifyDate -MediaCreateDate -MediaModifyDate -T -w+! %d/out.txt -r .
```

[More examples](https://exiftool.org/examples.html)

