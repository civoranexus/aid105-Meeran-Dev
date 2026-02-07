import { useState } from "react";
import UserForm from "../components/UserForm";
import SchemeList from "../components/SchemeList";
import { getRecommendations } from "../api/recommend";

export default function Home() {
  const [schemes, setSchemes] = useState([]);

  async function handleSubmit(user) {
    const data = await getRecommendations(user);
    setSchemes(data);
  }

  return (
    <>
      <UserForm onSubmit={handleSubmit} />
      <SchemeList schemes={schemes} />
    </>
  );
}
