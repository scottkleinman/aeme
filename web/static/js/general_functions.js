/*===================*/
/* General Functions */
/*===================*/

$(document).ready(function(){
	$('#about').click(function(event){
		event.preventDefault();
		$(".modal-title").html(about[0].title);
		$(".modal-body").html("<p>"+about[1].message+"</p>");
		zindex = $("#toolbarDiv").css("z-index") + 1;
		$("#navbarModal").css("z-index", zindex);
		$("#navbarModal").modal({
	  		backdrop: false
		});  
	});

	/* Opens metadata modal from navbar link */
	$("#metadata").click(function(){
		// sourceTEIheader should probably eventually be 
		// replaced with $("#currentFile").val()
		sourceTEIheader = "sampleteiHeader.xml";
		url = '/view/get-metadata'; // aeme/getsource
		$("#loading").show();
		$(".modal-title").html("Metadata");
		data = JSON.stringify([{'file': sourceTEIheader}]);
		$.ajax({
			url: url,
			type: 'POST',
			dataType: 'json',
			data: data,
			contentType: 'application/json;charset=UTF-8',
			complete: function(response) {
				response = JSON.parse(response["responseText"]);
				$("#navbarModalBody").html(response);
				$(".modal-body").css({"max-height": "600px", "overflow-y": "auto"});
				$("#loading").hide();
				c = $("#toolbarDiv").css("z-index");
				$("#navbarModal").css("z-index", c+1);
				$("#navbarModal").modal();
			},
			error: function() {
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
			}
		});
	});
});



