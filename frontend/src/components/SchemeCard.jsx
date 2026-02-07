export default function SchemeCard({ scheme }) {
  const color =
    scheme.category === "Highly Eligible" ? "green" :
    scheme.category === "Potentially Eligible" ? "orange" :
    "red";

  return (
    <div className={`scheme ${color}`}>
      <h3>{scheme.name}</h3>
      <p><b>Status:</b> {scheme.category}</p>
      <p><b>Eligibility:</b> {scheme.eligibility_score}%</p>
      <p>{scheme.benefits}</p>
    </div>
  );
}
