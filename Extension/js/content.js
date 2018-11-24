// document.body.style.background = 'yellow';
setTimeout(() => $(".im_dialog").on("click", () => {
	// $(".im_panel_peer_photo").click();
		var id = window.location.href.substring(33);
		console.log(id);
		var http = new XMLHttpRequest();
		var url = "https://ghw18.herokuapp.com/dialogue";
		var params = {
			"id": id
		};
		http.open("POST", url, true);
		http.setRequestHeader('Content-type', 'text/plain');
		http.send(id);
}), 5000);
