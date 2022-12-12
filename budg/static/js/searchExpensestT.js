function searchExpenses() {
  // Get the search query from the input field
  const query = document.getElementById("searchField").value;

  // Fetch the expense data from the API endpoint
  fetch("/expenses/search_expenses/")
    .then((response) => response.json())
    .then((data) => {
      // Filter the expenses based on the search query
      const results = data.filter((expense) => {
        return (
          expense.date.includes(query) ||
          expense.amount.toString().includes(query) ||
          expense.description.includes(query) ||
          expense.category.includes(query)
        );
      });

      // Display the search results on the page
      displayResults(searchRes);
    });
}

function displayResults(searchRes) {
  // Clear the previous search results and hide the other expenses
  document.getElementById("searchRes").innerHTML = "";
  document.getElementById("normalExpense").style.display = "none";

  // Loop through the results and display each expense
  searchRes.forEach((expense) => {
    const date = expense.date;
    const amount = expense.amount;
    const description = expense.description;
    const resultElement = document.createElement("div");
    resultElement.innerHTML = `
            <p>Date: ${date}</p>
            <p>Amount: ${amount}</p>
            <p>Description: ${description}</p>
          `;
    document.getElementById("searchRes").appendChild(resultElement);
  });
}
