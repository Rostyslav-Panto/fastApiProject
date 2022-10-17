const fetchDataBtn = document.querySelector("#count_data");

async function countData(csv_data) {
  try {
    console.log(csv_data)
    var checked = [];
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')

    for (var i = 0; i < checkboxes.length; i++) {
      checked.push(checkboxes[i].id)
    }
    console.log(checked)
    fetch(`/csv/${csv_data}/count/`, {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(checked)
    }).then(result=> {
      console.log(result)
      // location.replace(result.url);
      // return result

    })
  } catch (error) {
    console.log(error);
  }
}