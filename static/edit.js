const editForm = document.querySelector("#editForm");

editForm.addEventListener("submit", (e) => {
  e.preventDefault(); // Prevent the default form submission

  // Edit form data
  const formData = {
    id: item.id,
    name: editForm.querySelector("#name").value,
    creators: editForm.querySelector("#creators").value,
    casts: editForm.querySelector("#casts").value,
    year: editForm.querySelector("#year").value,
    summary: editForm.querySelector("#summary").value,
    img: editForm.querySelector("#img").value,
  };

  // Use the Fetch API to send the data
  fetch("/edit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
