const addForm = document.querySelector("#addForm");
const statusContainer = document.querySelector(".status_container");
let idIndex = names.length;

addForm.addEventListener("submit", (e) => {
  e.preventDefault(); // Prevent the default form submission

  // Collect form data
  const formData = {
    id: idIndex + 1,
    name: addForm.querySelector("#name").value,
    creators: addForm.querySelector("#creators").value,
    casts: addForm.querySelector("#casts").value,
    year: addForm.querySelector("#year").value,
    summary: addForm.querySelector("#summary").value,
    img: addForm.querySelector("#img").value,
  };

  // Use the Fetch API to send the data
  fetch("/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);

      // update id index from the updated number of data
      idIndex = data.count;

      // reset and refocus the form fields after submission
      addForm.reset();
      addForm.querySelector("#name").focus();

      // Show submission status and add the link to the View page for the new drama
      const container = document.createElement("div");
      container.classList.add("status");

      const status = document.createElement("p");
      status.innerText = `${formData.name.toUpperCase()} successfully added.`;

      const button = document.createElement("button");
      button.classList.add("btn");
      button.classList.add("btn-outline-success");
      button.textContent = `See ${formData.name.toUpperCase()} here`;
      button.addEventListener("click", () => {
        // direct to the view page for the added drama
        window.location.href = `view/${formData.id}`;
      });

      container.appendChild(status);
      container.appendChild(button);
      statusContainer.appendChild(container);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
