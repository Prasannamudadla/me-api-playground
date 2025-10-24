const API = "";



async function loadProfile(){
  const res = await fetch(`${API}/profile`);
  const p = await res.json();
  document.getElementById("name").innerText = p.name;
  document.getElementById("education").innerText = p.education;
  document.getElementById("skills").innerHTML = p.skills.map(s=>`<li>${s}</li>`).join('');

// Profile links: GitHub, LinkedIn, LeetCode
  document.getElementById("profile-links").innerHTML = `
    <p>
      <a href="${p.github}" target="_blank">GitHub</a> | 
      <a href="${p.linkedin}" target="_blank">LinkedIn</a> | 
      <a href="${p.leetcode}" target="_blank">LeetCode</a>
    </p>
  `;
}
async function loadProjects(){
  const skill = document.getElementById("search").value;
  const res = await fetch(`${API}/projects?skill=${skill}`);
  const data = await res.json();
  document.getElementById("projects").innerHTML = data.map(p => `
  <div class="project-card">
    <h4>${p.title}</h4>
    <p>${p.description}</p>
    <p><strong>Skills:</strong> ${p.skill}</p>
    <a href="${p.github_link}" target="_blank">GitHub Link</a>
  </div>
`).join('');

}
loadProfile(); loadProjects();
