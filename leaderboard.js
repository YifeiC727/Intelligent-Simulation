// Mini Leaderboard — renders in-game floating leaderboard
// Mock data; will be replaced by API call to /api/leaderboard/{level_id}

(function () {
  const MOCK_DATA = [
    { name: '机械臂达人', time: 118 },
    { name: '抓取高手', time: 165 },
    { name: '桌面整理王', time: 192 },
    { name: '码力全开', time: 222 },
    { name: '灵巧操控者', time: 255 },
  ];

  const MY_BEST = { rank: 7, time: 330 }; // null if never played

  const container = document.getElementById('miniLb');
  if (!container) return;

  function formatTime(s) {
    if (!s) return '--:--';
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return m + ':' + sec.toString().padStart(2, '0');
  }

  function render() {
    const rankClasses = ['gold', 'silver', 'bronze'];
    let html = '<div class="mini-lb-title">本关排行</div>';

    MOCK_DATA.forEach((player, i) => {
      const rankClass = rankClasses[i] || '';
      html += `<div class="mini-lb-row">
        <span class="mini-lb-rank ${rankClass}">${i + 1}</span>
        <span class="mini-lb-name">${player.name}</span>
        <span class="mini-lb-time">${formatTime(player.time)}</span>
      </div>`;
    });

    html += '<div class="mini-lb-divider"></div>';
    html += `<div class="mini-lb-row you-row">
      <span class="mini-lb-rank">${MY_BEST.rank ? '#' + MY_BEST.rank : '—'}</span>
      <span class="mini-lb-name you">我</span>
      <span class="mini-lb-time">${formatTime(MY_BEST.time)}</span>
    </div>`;

    container.innerHTML = html;
  }

  render();
})();
