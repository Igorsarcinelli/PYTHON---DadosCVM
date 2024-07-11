# CVM Data Fetching Application

## Description

This Python application was developed to fetch data from the Comissão de Valores Mobiliários (CVM) API. It extracts information about investment funds, providing a dataframe with the following data:

- **Fund CNPJ**: Used for fund identification.
- **Quotation Date**: The specific date of the fund's quotation.
- **Quota Value**: The value of the quota on the specified date.

These data are essential for creating analyses and visualizations over time, allowing detailed monitoring of the funds' performance.

## Features

- **Data Fetching**: Uses requests to the CVM API to obtain updated information on investment funds.
- **Data Formatting**: Organizes the fetched data into an easily manipulable dataframe.
- **Conditions**: Implements checks and conditions to ensure data accuracy and relevance.
- **Dataframe**: The output is structured in a dataframe with the columns Fund CNPJ, Quotation Date, and Quota Value.

## Contributions

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for more details.
