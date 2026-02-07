export default function UserForm({ onSubmit }) {
  const handleSubmit = e => {
    e.preventDefault();

    const data = new FormData(e.target);

    onSubmit({
      age: Number(data.get("age")),
      income: Number(data.get("income")),
      state: data.get("state"),
      categories: data.get("categories").split(",")
    });
  };

  return (
    <form onSubmit={handleSubmit} className="card">
      <h2>Citizen Profile</h2>

      <input name="age" placeholder="Age" required />
      <input name="income" placeholder="Annual Income" required />
      <input name="state" placeholder="State" required />
      <input name="categories" placeholder="Categories (comma separated)" />

      <button>Find Schemes</button>
    </form>
  );
}
