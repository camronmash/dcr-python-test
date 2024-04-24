## Adding New Columns to the Countries Table

In order to add new columns to the `countries` table, the following two SQL queries were executed in the SQLite command line tool:

```sql
ALTER TABLE countries ADD COLUMN topLevelDomain TEXT;
ALTER TABLE countries ADD COLUMN capital TEXT;
