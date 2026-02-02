export default function Response({ response }) {
  return (
    <p className="cortana-reply text-cyan-400 font-semibold mb-4">
      {response || "Cortana is ready"}
    </p>
  );
}
