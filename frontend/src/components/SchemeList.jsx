import SchemeCard from "./SchemeCard";

export default function SchemeList({ schemes }) {
  return (
    <div className="grid">
      {schemes.map(s => (
        <SchemeCard key={s.scheme_id} scheme={s} />
      ))}
    </div>
  );
}
