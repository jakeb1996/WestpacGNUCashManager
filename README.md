# Westpac QIF Converter for GNUCash

##### Notes
1. Details about the QIF format can be found here
https://www.w3.org/2000/10/swap/pim/qif-doc/QIF-doc.htm

2. Using the file names which are already described in this file will make copying and pasting each command easier. Notably, changing `<export_date>` is required.

3. Ensure CMD is in the directory which the Python files are located

##### 1. Export From Westpac
1. Go to Westpac Online Banking
2. Export each account separately as QIF
3. Move these files into `data/<export_date>`
4. Use these names: `raw_eSaver.qif`, `raw_choice.qif`


##### 2. Remove transfers between accounts
1. Run this command
You only need to do this to one account. As GNUCash is a double-entry booking system, it will reproduce the transactions we are about to remove. If we skip this step, we will see the transfer transactions twice causing errors in our data.
This command should be ran on the Choice QIF file to reduce the size of it

```
python remove-acc-tfr.py data/<export_date>/raw_choice.qif data/<export_date>/tfr_removed_choice.qif
```

##### 3. Convert to CSV
1. Run these commands in cmd:

```
python qif-to-csv.py data/<export_date>/raw_esaver.qif data/<export_date>/esaver.csv
```

```
python qif-to-csv.py data/<export_date>/tfr_removed_choice.qif data/<export_date>/choice.csv
```

##### 4. Make a copy of the new csv files
1. Run these commands in cmd:

```
copy data\<export_date>\esaver.csv data\<export_date>\esaver_labeled.csv
```

```
copy data\<export_date>\choice.csv data\<export_date>\choice_labeled.csv
```

##### 5. Process in Excel
1. Open `esaver_labeled.qif` and `choice_labeled.qif` in Excel
3. Remove row 1 which should read; `!Type:Bank`
2. Add a column before `column A`
3. Add the row number to the cells in column A. This will be used to sort the transactions back into the order they were exported in.
   That is; `A1 = 1, A2 = 2, A3 = 3, ..., A<n> = <n>`
4. Modify the column after the `L` flag accordingly. This is the category flag. You will see flags `D`, `M`, `T`, `L` and `^` in each row
5. If you have sorted the data during step 4, resort in ascending order on column `A` to return it to its original state
6. Remove `column A`
7. Add a row above `row 1` and put `!Type:Bank` into cell `A1`


##### 6. Convert back to QIF
1. Run these commands in cmd:

```
python csv-to-qif.py data/<export_date>/esaver_labeled.csv data/<export_date>/esaver_labeled.qif
```

```
python csv-to-qif.py data/<export_date>/choice_labeled.csv data/<export_date>/choice_labeled.qif
```

2. IMPORTANT: Open both files and remove the commas on line 1.
   Line 1 should only read: `!Type:Bank`


##### 7. Import into GNUCash
1. Open your GNUCash cash file
2. Select File->Import->QIF
3. Use the `choice_labeled.qif` and `esaver_labeled.qif` files
4. Enter your account names;
`
Assets:Westpac eSaver
`
`
Assets:Westpac Choice
`

5. Follow the prompts

##### Done!