const API_URL = "http://127.0.0.1:8000/jobs";

// hämta jobb från api
async function fetchJobs() {
  const res = await fetch(API_URL);
  const jobs = await res.json();

  const list = document.getElementById("jobList");
  list.innerHTML = "";

  jobs.forEach(job => {
    const li = document.createElement("li");

    li.innerHTML = `
    <div class="job-info">
        <strong>${job.company}</strong> - ${job.role} (${job.status})
    </div>
    
    <div class="job-actions">
        <button onclick="deleteJob(${job.id})">Delete</button>
        <button onclick="updateJob(${job.id})">Mark Interview</button>
    </div>
    `;

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
async function deleteJob(id) {
    await fetch(`${API_URL}/${id}`, {
      method: "DELETE"
    });
  
    fetchJobs();
  }

// update till interview
async function updateJob(id) {
    const res = await fetch(API_URL);
    const jobs = await res.json();
  
    const job = jobs.find(j => j.id === id);
  
    await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        company: job.company,
        role: job.role,
        status: "Interview"
      })
    });
  
    fetchJobs();
  }