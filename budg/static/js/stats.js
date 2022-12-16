const renderChart = (data, lables) => {
  var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "6 month expnese",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 135, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(151, 102, 132, 1)",
            "rgba(153, 99, 132, 1)",
            "rgba(255, 159, 64, 1)",
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 135, 1)",
            "rgba(25, 206, 86, 1)",
            "rgba(211, 192, 192, 1)",
            "rgba(234, 102, 132, 1)",
            "rgba(153, 99, 132, 1)",
            "rgba(255, 159, 64, 1)",
            "gree",
            "yellow",
          ],

          borderColor: [
            "rgba(54, 162, 135, 1)",
            "rgba(25, 206, 86, 1)",
            "rgba(211, 192, 192, 1)",
            "rgba(234, 102, 132, 1)",
            "rgba(153, 99, 132, 1)",
            "rgba(255, 159, 64, 1)",
          ],

          borderWidth: 1,
        },
      ],
    },

    options: {
      title: {
        display: true,
        text: "Expenses by Category ",
      },
    },
  });
};

const getChartData=()=>{
    fetch
}
document.onload=getChartData
