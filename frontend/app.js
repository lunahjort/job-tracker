const API_URL = "http://127.0.0.1:8000/jobs";

// hämta jobb från API
// lägg till knappar för delete och update + ändring för rendering
async function fetchJobs() {
    const res = await fetch(API_URL);
    const jobs = await res.json();
  
    const list = document.getElementById("jobList");
    list.innerHTML = "";
  
    jobs.forEach(job => {
      const li = document.createElement("li");
      li.textContent = `${job.company} - ${job.role} (${job.status})`;
      list.appendChild(li);
    });
}

fetchJobs();

// POST
const form = document.getElementById("jobForm");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const company = document.getElementById("company").value;
  const role = document.getElementById("role").value;
  const status = document.getElementById("status").value;

  await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ company, role, status })
  });

  form.reset();
  fetchJobs();
});

// async delete-funktion

// update till interview?