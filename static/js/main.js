const fetchDataBtn = document.querySelector("#fetch_data");

async function getData() {
  try {
    const jsonResult = await paginated_fetch("https://swapi.dev/api/people/");
    console.log(jsonResult)
    fetch("/fetch_csv/", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(jsonResult)
    }).then(result => {
      console.log("Request complete! response:", result);
    });
  } catch (error) {
    console.log(error);
  }
}

fetchDataBtn.addEventListener("click", getData);

// Recursive pagination. We have number of elements in start response so could be implemented using iteration
function paginated_fetch(
  url = is_required("url"),
  previousResponse = []
) {
  return fetch(url)
    .then(response => response.json())
    .then(newResponse => {
      console.log(newResponse)
      const response = [...previousResponse, ...newResponse.results];

      if (newResponse.next) {
        return paginated_fetch(newResponse.next, response);
      }

      return response;
    });
}