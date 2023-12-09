## Getting Set Up

To run the test example, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/leunoia/DataProcessing.git
    ```

2. Navigate to the project directory:
    ```bash
    cd DataProcessing
    ```
3. Run example script:
    ```bash
    python database.py
    ```

## Importing the Database Class

To import the `Database` class into another Python file, follow these steps:

1. Make sure you have cloned the repository and then create another directory at the same level as DataProcessing.



2. In your Python file, add the following import statement:
    ```python
    from DataProcessing import Database
    ```

3. Create an instance of the `Database` class:
    ```python
    db = Database()
    ```

4. You can now use the `db` instance to perform atomic operations on your data set.


## Write-Up for assignment improvements

Overall, I think this is a good assignment and would recommend it being given to future students. One improvement I could imagine would be to have some sort of data source that students can use to test their database. This could be a simple csv file or something else that is easily parse. This way they could raad it into their database programatically and see how it performs.

