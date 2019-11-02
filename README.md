# add-budget-categories
Add budget categories to Rabobank transactions.

In Excel I keep track of my income and expenses. For this reason, I regularly download all transactions of my current account via Rabobank Internet Banking.

The purpose of this Python script is to add a budget category to all transactions that were downloaded, so I don't have to do this manually.

As a precondition, these downloaded transactions should be present in the file 'C:/Users/adriv/Downloads/transacties.csv'.

The script will duplicate the file in the same directory, called 'processedTransacties.csv'. This is the file for which an aditional column called 'Categorie' will be added and populated for every transaction.

After execution, the newly created file can be imported in the Excel used for capturing and gain insights in income and expenses.
