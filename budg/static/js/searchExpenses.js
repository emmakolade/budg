const searchField = document.querySelector("#searchField");
const outputHide = document.querySelector(".expense-hide");
const transactionhide = document.querySelector(".transaction-history");

outputHide.style.display = "none";

searchField.addEventListener("keyup", (e) => {
  const searchValue = e.target.value;

  if (searchValue.trim().lenght > 0) {
    fetch("/expenses/search_expenses/", {
      body: JSON.stringify({ seatchText: searchValue }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        transactionhide.style.display = "none"
        outputHide.style.display = "block";
        if (data.length === 0) {
          outputHide.innerHTML="no result found"
        }
      });
  }
});
