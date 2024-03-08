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

  // Use the Fetch API to update the data
  fetch(`/edit/${item.id}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      // Redirect to the view page for the edited item
      window.location.href = `/view/${item.id}`;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

// Discard changes Button with confirmation from users
document.querySelector("#discard-btn").addEventListener("click", () => {
  const userConfirmation = confirm("Are you sure you want to discard changes?");
  if (userConfirmation) {
    window.location.href = `/view/${item.id}`;
  }
});
