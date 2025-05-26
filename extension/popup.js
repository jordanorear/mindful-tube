document.getElementById("searchButton").addEventListener("click", async () => {
  const query = document.getElementById("searchInput").value;
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  const res = await fetch(`https://mindful-tube.onrender.com/search?q=${encodeURIComponent(query)}`);
  const data = await res.json();

  if (data.items && data.items.length > 0) {
    const video = data.items[0];
    const videoId = video.id.videoId;
    const iframe = document.createElement("iframe");
    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`;
    iframe.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
    iframe.allowFullscreen = true;
    resultsDiv.appendChild(iframe);

    // Clear search input to encourage 1-video-at-a-time use
    document.getElementById("searchInput").value = "";
  } else {
    resultsDiv.innerHTML = "<p>No results found.</p>";
  }
});