// $(document).ready(function() {
// 	/* ======= Highlight.js Plugin ======= */ 
//     /* Ref: https://highlightjs.org/usage/ */     
//     $('pre code').each(function(i, block) {
// 	    hljs.highlightBlock(block);
// 	 });

// });

// share links
function FBshare() {
	window.open("https://www.facebook.com/sharer.php?title="+document.title+"u="+document.URL);
}
function TTshare() {
	window.open("https://twitter.com/intent/tweet?text="+document.title+"&url="+document.URL);
}
function WAshare() {
	window.open("https://web.whatsapp.com/send?text="+document.title+" | "+document.URL);
}
function Emailshare() {
	window.open("mailto:?subject="+document.title+"&body="+document.URL);
}


$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })