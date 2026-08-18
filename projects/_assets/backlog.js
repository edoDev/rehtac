async function renderBacklog(targetId) {
  const el = document.getElementById(targetId);
  if (!el) return;
  try {
    const res = await fetch("BACKLOG.md", { cache: "no-store" });
    if (!res.ok) throw new Error(String(res.status));
    el.textContent = await res.text();
  } catch (err) {
    el.textContent = "Could not load BACKLOG.md (" + err.message + "). Open the markdown file in the repo.";
  }
}
renderBacklog("backlog");
