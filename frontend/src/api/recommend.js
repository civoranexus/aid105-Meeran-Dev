export async function getRecommendations(user) {
  const res = await fetch("http://localhost:5000/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user)
  });

  return await res.json();
}
