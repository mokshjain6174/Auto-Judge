function predict() {
  const description = document.getElementById("description").value;
  const inputDesc = document.getElementById("input_desc").value;
  const outputDesc = document.getElementById("output_desc").value;

  if (!description || !inputDesc || !outputDesc) {
    alert("Please fill all fields!");
    return;
  }

  const payload = {
    description: description,
    input_description: inputDesc,
    output_description: outputDesc
  };

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("difficulty").innerText = data.class;
    document.getElementById("score").innerText = data.score;
  })
  .catch(error => {
    console.error(error);
    alert("Backend not running");
  });
}
