const updateHuman = async(url, element) => {
    const sensorData = await fetch(url)
        .then(response => response.text())
    const target = document.getElementById(element);
    
    if(sensorData > 5) {
        target.innerHTML = `<h1>画面を切って下さい！</h1>`;
    }
    else {
        target.innerHTML = `<h1>PCの前に人を検知しています。</h1>`;
    }
}

// 自動更新
function doReload() {
    window.location.reload();
}
window.addEventListener('load',function(){
    setTimeout(doReload, 1000);
});
