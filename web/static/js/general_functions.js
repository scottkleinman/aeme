/*===================*/
/* General Functions */
/*===================*/

/* about() -- Opens about modal from navbar link */
function about() {
	msg = "This is a demonstration of the digital edition platform for the Archive of Early Middle English. This is an alpha version used for development purposes. Any texts currently loaded are incomplete fragments used to test functionality. The images of Junius 1 are JPEGs tiled on the  fly, so there may be a delay before they appear.";
	$(".modal-title").html("About this Site");
	$(".modal-body").html("<p>"+msg+"</p>");
	zindex = $("#toolbarDiv").css("z-index") + 1;
	$("#navbarModal").css("z-index", zindex);
	$("#navbarModal").modal({
	  backdrop: false
	});  
}

/* metadata() -- Opens metadata modal from navbar link */
function metadata() {
	var box = bootbox.alert({
		size: "small",
		title: "Metadata",
		message: "Questa funzione non è ancora attiva. E alla fine mostrare il contenuto dal <code>teiHeader</code>."
	}).draggable({
		handle: ".panel-heading"}
	);
	box.find(".modal-content").addClass("panel-danger");
	box.find(".modal-header").addClass("panel-heading");
	c = $("#toolbarDiv").css("z-index");
	$(".bootbox").css("z-index", c+1); 
}
