/*===================*/
/* General Functions */
/*===================*/

$(document).ready(function(){
	/* Opens metadata modal from navbar link */
	$("#metadata").click(function(){
		var box = bootbox.alert({
			size: "small",
			title: metadata[0]["title"],
			message: metadata[1]["message"]
		}).draggable({
			handle: ".panel-heading"}
		);
		box.find(".modal-content").addClass("panel-danger");
		box.find(".modal-header").addClass("panel-heading");
		c = $("#toolbarDiv").css("z-index");
		$(".bootbox").css("z-index", c+1); 
	});
});