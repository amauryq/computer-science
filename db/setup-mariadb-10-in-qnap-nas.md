# Setup MariaDB v10 in QNAP NAS

## Configure DbVisualizer

Follow references to install Maria DB 10 and next open an ssh session on the server

```sh
`getcfg MariaDB10 Install_Path -f /etc/config/qpkg.conf`/bin/mysql -u root -p  -h localhost -S /var/run/mariadb10.sock -P 3307
```

Grant priviledges to your user for working remote, make sure specify your desired password

```sql
MariaDB [(none)] GRANT ALL PRIVILEGES ON *.* TO 'amauryq'@'%' IDENTIFIED BY 'youPassWot';FLUSH PRIVILEGES;
```

Then install [DbVisualizer](https://www.dbvis.com/) or if you are in Mac

```sh
brew dbvisualizer
```

Create a new connection in DbVisualizer with the parameter you used to install MariaDB

## Create DB for Tax related queries

```sql
create database minttxs;

use minttxs;

create table minttxs (
  date DATE,
  description VARCHAR(255),
  original_description VARCHAR(255),
  amount FLOAT,
  transaction_type VARCHAR(25),
  category VARCHAR(255),
  account_name VARCHAR(255),
  labels VARCHAR(255),
  notes VARCHAR(512)
);
```

Upload the csv file you want to import with the transactions

Load data into the table

```sql
LOAD DATA INFILE '/share/CACHEDEV2_DATA/.qpkg/MariaDB10/mint-transactions.csv'
INTO TABLE minttxs
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@date, description, original_description, amount, transaction_type, category, account_name, labels, notes)
SET date=STR_TO_DATE(@date, '%m/%d/%Y');
```

## Extract data using Queries

```sql
use minttxs;

select count(*) from minttxs;

select category, round(sum(amount)) as total_amount
from minttxs
where year(date) = 2023 and transaction_type = 'debit'
group by category;

with the_rows as 
(select * from minttxs
where year(date) = 2023 and (description like '%Lakeview%' or description like '%Renovations Property%')
order by date ASC)
select sum(the_rows.amount) as total_amount from the_rows
```

## References

[How to access MariaDB remotely](https://www.qnap.com/en-in/how-to/faq/article/how-to-access-mariadb-remotely)
