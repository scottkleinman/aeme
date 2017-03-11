var debug = false;
var noImage = false;

function loadTileSources (response, url) {
	var numPages = 0;
	var tileSources = [];
	var pagination = response["responseJSON"].pagination;
	$.each(pagination, function(k, v) {
		option = '<option value="'+k+'" data-facs="'+v[1]+'">'+v[0]+'</option>';
	    $("#pagerSelect").append(option);
	    numPages += 1;
	    // The url is assumed to be a relative path beginning with the MS
	    var ms = url.split("/")[0];
	    var domain = "http://tsar192.grid.csun.edu/";
	    switch(ms) {
	    	// Bodleian, Junius 1
	    	case "bodljunius1":
	    	sources = domain + "junius1/"+v[1]+".dzi";
	    	break; 

	    	// Bodleian, Laud Misc. 108
	    	case "bodllaudmisc108":
	    	sources = domain + "laudmisc108/dzc_output_images/"+v[1]+".xml";
	    	break; 

	    	// British Library, Harley 2250
	    	case "harley2250":
	    	sources = domain + "harley2250/"+v[1]+".dzi";
	    	break;
	    }
	    tileSources.push(sources);
	});
	return tileSources;
}

function loadText(url, viewer) {
	$('#left-panel').removeClass('edit');
	data = JSON.stringify([{'title': url}]);
	// If the noImage is false, load the tile sources
	$.ajax({
		url: site_url+"/load-text",
		type: 'POST',
		dataType: 'json',
        data: data,
        contentType: 'application/json;charset=UTF-8',
        cache: false,
        beforeSend: function() {
        	$("#loading").show();
        },
		complete: function(response) {
			// Empty and re-populate the folio dropdown
			$(".selectpicker").empty();
			tileSources = loadTileSources(response, url);
			// Otherwise, load the default image
			if (noImage == true) {
				tileSources = [{
			        type: 'image',
			        url:  'static/images/AEME_logo_final_small2.jpg'		
				}];
			}
		    viewer.open(tileSources);
		    $(".openseadragon-container").css("position", "absolute");
			$("#debugNumPages").html(numPages);
			$("#currentFile").val(url);
			$("#currentPageIndex").html(0);
			$("#numPages").val(numPages);
			$("#currentPageIndex").val(0);
			$("#pagerSelect").children().first().attr("selected", "selected");
			$('#pagerSelect').selectpicker('refresh');
			// Set the initial view to critical
			$(".lazyload").remove();
			LazyLoad.css('static/css/critical.css', function () {
				$("input[value='critical']").checked = true;
				$('#currentView').val('critical');
				$('#criticalView').parents('.btn').button('toggle');
				$("#viewStyles").attr("href", "static/css/critical.css");
			});
			// Populate the left panel text
			$("#left-panel").empty().append(response["responseJSON"].html_pages);
			var wrapperContent = '<button id="canceledit" type="button" class="btn btn-primary pull-right" style="margin-bottom:5px; margin-left:5px;">Cancel</button><button id="saveme" type="button" class="btn btn-primary pull-right" style="margin-bottom:5px;">Save Changes</button><pre id="editor"></pre>';
			$("#left-panel").append('<div id="edit-wrapper" style="display:none;">'+wrapperContent+'</div>');
			$("#editor").text(response["responseJSON"].xmlstr);
			$("#source").text(response["responseJSON"].xmlstr);
			$("#filepath").text(response["responseJSON"].filepath);
			var editor = ace.edit("editor");
			//editor.session.reset();
			//editor.session.resetCaches();
			editor.session.setMode("ace/mode/xml");
			editor.setTheme("ace/theme/tomorrow");
			// enable autocompletion and snippets
			editor.setOptions({
			    enableBasicAutocompletion: true,
			    enableSnippets: true,
			    enableLiveAutocompletion: false,
			    fontSize: "12pt"
			});
			editor.gotoLine(1);
			$('#left-panel-container').perfectScrollbar('update');
			moveNotes();
			$("#loading").hide();
		}
	});
}

/* This function handles a bunch of positioning rules for marginal elements.
   Each element position is measured inline and then element is re-positioned 
   relative to the margin and its inline height. */
function moveNotes() {
	if ($("#currentView").val() != "critical") {
		$("tei-ab[place=marginLeft]").each(function(){
			position = $(this).position();
			$(this).css({"position":"absolute", "left":2})
		});
		$("tei-ab[place=marginRight]").each(function(){
			position = $(this).position();
			$(this).css({"position":"absolute", "right":50})
		});
		$("tei-add[place=marginLeft]").each(function(){
			position = $(this).position();
			$(this).css({"position":"absolute", "left":2})
		});
		$("tei-add[place=marginRight]").each(function(){
			position = $(this).position();
			$(this).css({"position":"absolute", "right":50})
		});
	}

	/* Notes have to be put inside <l> if they are to be positioned inline with it. */
	$("tei-note").each(function(index) {
		// Create a note id
		$(this).attr("id", index);
		// Create a corresponding ref
		ptr = "#"+index;
		// Insert a ptr
		$('<ptr ref="'+ptr+'"/>').insertBefore($(this));
		// Get the ptr's position
		position = $(ptr).position();
		// Detach the note
		note = $(this).detach();
		// Append the note to the div1
		note.appendTo("tei-div1");
		// Position the note relative to the ptr
		note.css({"position": "absolute", "top": position.top, "right": 20})
	});
}

function loadPage(page) {
	data = JSON.stringify([{'page': page}]);
	$.ajax({
		url: site_url+"/load-page",
		type: 'POST',
		dataType: 'json',
        data: data,
        contentType: 'application/json;charset=UTF-8',
        cache: false,
        beforeSend: function() {
        	$("#loading").show();
        },
		complete: function(response) {
			// Populate the left panel text
			$("#left-panel").empty().append(response["responseJSON"].html_pages);
			//console.log(response["responseJSON"].html_pages);
			var wrapperContent = '<button id="canceledit" type="button" class="btn btn-primary pull-right" style="margin-bottom:5px; margin-left:5px;">Cancel</button><button id="saveme" type="button" class="btn btn-primary pull-right" style="margin-bottom:5px;">Save Changes</button><pre id="editor"></pre>';
			$("#left-panel").append('<div id="edit-wrapper" style="display:none;">'+wrapperContent+'</div>');
			$("#editor").text($("#source").text());
			$("#filepath").text(response["responseJSON"].filepath);
			var editor = ace.edit("editor");
			editor.session.setMode("ace/mode/xml");
			editor.setTheme("ace/theme/tomorrow");
			// enable autocompletion and snippets
			editor.setOptions({
			    enableBasicAutocompletion: true,
			    enableSnippets: true,
			    enableLiveAutocompletion: false,
			    fontSize: "12pt"
			});
			n = $('tei-span').children().first().attr("n");
			s = 'pb n="'+n;
			editor.find(s, {wrap: true}, false);
			row = editor.getCursorPosition().row; 
			$('#left-panel-container').perfectScrollbar('update');
			moveNotes();
			$("#loading").hide();
		}
	});
}

$(document).ready(function() {
	if (debug == true) {$("#debug").show();}
	$('#left-panel-container').perfectScrollbar();

	/* Handle panel resizing */
	var i = 0;
	// Handle click on the dragbar
	$('#dragbar').mousedown(function(e) {
		e.preventDefault();
		// Resize the column based on mouse position
		$(document).mousemove(function(e) {
			$('#left-panel-container').css("width", e.pageX+2);
		    $('#right-panel-container').css("width", e.pageX-2);
		    $('#right-panel').css("left", e.pageX-2);
		});
	});
	// Stop resizing when the dragbar is unclicked
	$(document).mouseup(function(e) {
       $('#left-panel-container').perfectScrollbar('update');
	   $(document).unbind('mousemove');
	});

    /* Enable Bootstrap modal drag functionality -- relies on jQuery UI */
    $(".modal-dialog").draggable({handle: ".modal-header"});	
		
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

	$(".navLink").click(function(e) {
		e.preventDefault();
		loadText($(this).attr("href"), viewer); // Load the text
		// Load the image
		// Call function here.
		//This was some code to handle the loading the IIIF sample
		//if ($(this).attr("href")=="IIIF") { changeImage('IIIF', '1'); }
		$("#loading").hide();
	});

	/* Page Select Dropdown Menu */

	// Populate the Menu on Initial Load
	$.each(pagination, function(key, value) {
		option = '<option value="'+key+'" data-facs="'+value[1]+'">'+value[0]+'</option>';
	    $("#pagerSelect").append(option);
	});
	$("#pagerSelect").children().first().attr("selected", "selected");	

	// Handle User Changes to the Menu
	$('#pagerSelect').on('changed.bs.select', function(e) {
		pageIndex = $(this).val() - 1;
		$("#loading").show();
		setTimeout(function() { $("#loading").hide(); }, 3000);
		loadPage(pageIndex);
		$("#currentPageIndex").val(pageIndex); // prevPageIndex
		$("#debugCurrentPageIndex").html(pageIndex);
		$("#left-panel").html(text[pageIndex]);
		$('#left-panel-container').perfectScrollbar('update');
	  	viewer.goToPage(pageIndex); // Update the manuscript viewer
	});

	/* OpenSeadragon Toolbar Buttons */
	// Zoom In
	$("#zoom-in").click(function(event) {
		event.preventDefault();
		viewer.viewport.zoomBy(1.5);
	});

	// Zoom Out
	$("#zoom-out").click(function(event) {
		event.preventDefault();
		viewer.viewport.zoomBy(.5);
	});

	// Home
	$("#home").click(function(event) {
		event.preventDefault();
		viewer.viewport.goHome(true);
	});

	// Full Page
	$("#full-page").click(function(event) {
		event.preventDefault();
		if (viewer.isFullPage() == false) {
			viewer.setFullPage(true);
		}
		else { viewer.setFullPage(false); }
	});

	// Show warning when the user navigates to page 0 or numPages + 1
	function outOfRange() {
		var box = bootbox.alert({
			size: "small",
			title: "Attenzione!",
			message: "Non ci sono pi&ugrave; pagine."
		});
		box.find(".modal-content").addClass("panel-danger");
		box.find(".modal-header").addClass("panel-heading");
		c = $("#toolbarDiv").css("z-index");
		$(".bootbox").css("z-index", c+1);		
	}

	// Previous
	$("#previous").click(function(event) {
		event.preventDefault();
		var currentPageIndex = parseInt($("#currentPageIndex").val());
		if (currentPageIndex == 0) { outOfRange(); } // Show error
		else {
			$("#loading").show();
			setTimeout(function() { $("#loading").hide(); }, 3000);
			var prevPageIndex = currentPageIndex - 1;
			var folioMenuIndex = currentPageIndex;
			loadPage(prevPageIndex);
			$('#pagerSelect').find('[value='+folioMenuIndex+']').attr("selected", "selected");
			$('#pagerSelect').selectpicker('val', folioMenuIndex);
			$('#pagerSelect').selectpicker('refresh');
			$("#currentPageIndex").val(prevPageIndex);
			$("#debugCurrentPageIndex").html(prevPageIndex);
			$("#left-panel").html(text[prevPageIndex]);
			$('#left-panel-container').perfectScrollbar('update');
		}
	}); 

	// Next
	$("#next").click(function(event) {
		event.preventDefault();
		var currentPageIndex = parseInt($("#currentPageIndex").val());
		var numPages = parseInt($("#numPages").val());
		if (currentPageIndex == numPages-1) { outOfRange(); } // Show error
		else {
			$("#loading").show();
			setTimeout(function() { $("#loading").hide(); }, 3000);
			var nextPageIndex = currentPageIndex + 1;
			var folioMenuIndex = nextPageIndex + 1;
			loadPage(nextPageIndex);
			$('#pagerSelect').find('[value='+folioMenuIndex+']').attr("selected", "selected");
			$('#pagerSelect').selectpicker('val', folioMenuIndex);
			$('#pagerSelect').selectpicker('refresh');
			$("#currentPageIndex").val(nextPageIndex);
			$("#debugCurrentPageIndex").html(nextPageIndex);
			$("#left-panel").html(text[nextPageIndex]);
			$('#left-panel-container').perfectScrollbar('update');
		}
	}); 

	/* Bootstrap Popovers */
	$('[data-toggle="popover"]').popover();

	/* Bootstrap Tooltips */
	$(document).on('mouseenter', 'tei-name', function(e) {
		$(this).tooltip({
		  	"html": true,
		  	"title": function(e){
		  		return "Type: "+$(this).attr("type")+"<br>Ref: "+ $(this).attr("ref");
		  	}
		});
	});

	/* Notes */
	$(document).on("click", ".note", function(e) {
		$("#noteModalLabel").html($(this).attr("data-title"));
		$("#noteModalBody").html($(this).attr("data-content"));
		c = $("#toolbarDiv").css("z-index");
		$("#noteModal").css("z-index", c+1);
		$("#noteModal").modal({
			backdrop: false
		});  
	});	


	/* This small routine makes individual words clickable. However, it leaves 
	too much white space clickable. */
	$(document).on("click", "tei-ab, tei-l, tei-p", function(e) {
        var s = window.getSelection();
        s.modify('extend','backward','word');        
        var b = s.toString();
        s.modify('extend','forward','word');
        var a = s.toString();
        s.modify('move','forward','character');
        word = b+a;
        /* It's better to load with Ajax because you can add a loading icon */
        /* It would be possible to loop through variations on the word and substrings
           until results are returned. */
        url = 'http://quod.lib.umich.edu/cgi/m/mec/med-idx?size=First+100&type=orths&q1='+word+'*&rgxp=constrained';
		$("#navbarModalLabel.modal-content").css("width", "700px");
		f = '<p><a href="http://quod.lib.umich.edu/m/med/lookup.html" target="_blank">Search the MED in a new tab</a></p>';
		f += '<iframe src="'+url+'" style="zoom:0.60" width="99.6%" height="250" frameborder="0"></iframe>';
		$("#navbarModalBody").html(f);
		c = $("#toolbarDiv").css("z-index");
		$("#navbarModal").css("z-index", c+1);
		$("#navbarModal .modal-title").html("<em>Middle English Dictionary</em> Entry");
		$("#navbarModal").modal();
    });

	/* Handle Changes to the View */
	$(".viewselect").click(function() {
		switch(true) {
			// Call Critical Stylesheet
			//case $(this).children().val() == 'critical':
			case $(this).attr("id") == 'critical':
				$("#loading").show().delay(3000);
				$(".lazyload").remove();
				LazyLoad.css('static/css/critical.css', function () {
					$('#currentView').val('critical');
					$("tei-div1").each(function() {
						// Handle long-line-prose
						if ($(this).attr("rend") == "long-line-prose") {
							$("tei-l").removeClass("long-line-prose");
							$("tei-l").css({"display": "block", "margin-left": "4em"});
							$("tei-l").each(function() {
								$(this).parent().css({"left": 0, "position": "static"});
							});
						}
						if ($(this).attr("rend") == "halfline") {
							$("tei-l").removeClass("A-verse");
							$("tei-l").removeClass("B-verse");
							$("tei-l").css({"display": "block", "margin-left": "4em"});
						}
					});
					$(".viewselect").removeClass('active');
					$("#critical").addClass('active');
					hideEditor("#critical");
					$("#loading").hide();
				});
				break;
			// Call Diplomatic Stylesheet
			case $(this).attr("id") == 'diplomatic':
				$("#loading").show().delay(3000);
				$(".lazyload").remove();
				LazyLoad.css('static/css/diplomatic.css', function () {
					// Add columns if necessary
					// This seems to be an attempt to divide the screen into three columns?
					// html_page = $("#left-panel").html();
					// console.log(html_page);
					// if (html_page.match(/<tei-cb n=\"2\"><\/tei-cb>/)) {
					// 	html_page = html_page.replace('<tei-cb n="1"></tei-cb>', '');
					// 	html_page = html_page.split(/<tei-cb n=\"2\"><\/tei-cb>/);
					// }
					// $("#left-panel").html('<div class="row"><div id="col-a" class="col-md-6"></div><div id="col-b" class="col-md-6"></div></div>');
					// $("#col-a").html(html_page[0]);
					// $("#col-b").html(html_page[1]);
					// console.log(html_page[0]);
					// console.log(html_page[1]);

					$('#currentView').val('diplomatic');
					// NB. This should probably on lg, not div1
					$("tei-div1").each(function() {
						// Handle long-line-prose
						if ($(this).attr("rend") == "long-line-prose") {
							$("tei-l").each(function() {
								//$(this).parent().addClass($(this).attr("rhyme")+"-verse");
								$(this).parent().css({"left": "4em", "position": "absolute"});
								$(this).css({"display": "inline", "margin-left": 0});
							});
							$("tei-l").addClass("long-line-prose");
						}
						// Handle halfline collapsing
						if ($(this).attr("rend") == "halfline") {
							$("tei-l").each(function() {
								rhyme = $(this).attr("rhyme");
								$(this).addClass(rhyme+"-verse");
							});
							$("tei-l.B-verse").css("margin-left", 0);
							$("tei-l").css("display", "inline");
						}
					});
					$(".viewselect").removeClass('active');
					$("#diplomatic").addClass('active');
					hideEditor("#diplomatic");
					$("#loading").hide();
				});
				break;
			// Call Proofreading Stylesheet
			case $(this).attr("id") == 'proofreading':
				$('#currentView').val('proofreading');
				$("#loading").show().delay(3000);
				$(".lazyload").remove();
				/* The proofreading stylesheet needs some work. */
/*				LazyLoad.css('static/css/proofreading.css', function () {
					$('#currentView').val('proofreading');
					$("#viewStyles").attr("href", "static/css/proofreading.css");
					$("tei-title").show();
					// NB. This should probably on lg, not div1
					$("tei-div1").each(function() {
						// Handle long-line-prose
						if ($(this).attr("rend") == "long-line-prose") {
							$("tei-l").each(function() {
								//$(this).parent().addClass($(this).attr("rhyme")+"-verse");
								$(this).parent().css({"left": "4em", "position": "absolute"});
								$(this).css({"display": "inline", "margin-left": 0});
							});
							$("tei-l").addClass("long-line-prose");
						}
						// Handle halfline collapsing
						if ($(this).attr("rend") == "halfline") {
							$("tei-l").each(function() {
								rhyme = $(this).attr("rhyme");
								$(this).addClass(rhyme+"-verse");
							});
							$("tei-l.B-verse").css({"display": "inline", "margin-left": 0});
							$("tei-l").css("display", "inline");
						}
					});
				});
*/
					$(".viewselect").removeClass('active');
					$("#proofreading").addClass('active');
					hideEditor("#proofreading");
					$("#loading").hide();
				break;
			// Call Edit Mode
			case $(this).attr("id") == 'edit':
				var previousView = "#"+$('#currentView').val();
			    if ($("#left-panel").hasClass('edit')) {
					hideEditor(previousView);
			    }
			    else {
					showEditor(previousView);
			    }
			    break;			
			// Call Source Code
			case $(this).children().attr("id") == 'source':
			// Need to get the title somehow			        
				data = JSON.stringify([{'url': $("#currentFile").val()}]);
				$("#loading").show();
				url = 'get-source'; // aeme/getsource
				$(".modal-title").html("XML Source");
				$.ajax({
					url: url,
					type: 'POST',
					dataType: 'text',
					data: data,
                    contentType: 'application/json;charset=UTF-8',
                    cache: false,
					//dataFilter: function(data, type) {
						// console.log(type);
						// console.log(data);
					//},
					complete: function(xhr, status) {
						// console.log(status);
						// console.log(xhr);
						xmlStr = xhr.responseText;
						//console.log(xmlStr);
						xmlStr = vkbeautify.xml(xmlStr, 4);
						$("#navbarModalLabel.modal-content").css("width", "700px");
						$("#navbarModalBody").html('<textarea style="width:100%;height:500px;">'+xmlStr+'</textarea>');
						$("#loading").hide();
					}
				});
				c = $("#toolbarDiv").css("z-index");
				$("#navbarModal").css("z-index", c+1);
				$("#navbarModal").modal();
				break;
			default:
				var box = bootbox.alert({
					size: "small",
					title: "Attenzione!",
					message: "AEME Viewer non riconosce la funzione richiesta."
				});
				box.find(".modal-content").addClass("panel-danger");
				box.find(".modal-header").addClass("panel-heading");
				c = $("#toolbarDiv").css("z-index");
				$(".bootbox").css("z-index", c+1);
		}
	});

	function showEditor(view) {
		$(view).removeClass('active');
		//$('#currentView').val('edit');
		$('#left-panel').addClass('edit');
		$('#left-panel').children().first().css("display", "none");
		$('#edit-wrapper').css("display", "block");
	}

	function hideEditor(view) {
		$(view).addClass('active');					
		$("#edit").removeClass('active').blur();
		$('#left-panel').removeClass('edit');
		$('#edit-wrapper').css("display", "none");
		$('#left-panel').children().first().css("display", "block");
	}

	/* Load Initial Image */
	if (noImage == true) {
		tileSources = [{
	        type: 'image',
	        url:  'static/images/AEME_logo_final_small2.jpg'		
		}];
	}

	var osd_options = {
        id:             "canvas",
        prefixUrl:      "static/lib/openseadragon/images/",
        tileSources: tileSources,
        sequenceMode:   true,
        showNavigationControl: false,
        toolbar:        "toolbarDiv",
        showNavigator:   false,
        zoomInButton:   "zoom-in",
        zoomOutButton:  "zoom-out",
        homeButton:     "home",
        fullPageButton: "full-page",
        nextButton:     "next",
        previousButton: "previous"
       //defaultZoomLevel:   1
        //resize: true
        //preserveViewport: true
        //visibilityRatio: 1,
        //showNavigationControl: false			
	}
    var viewer = OpenSeadragon(osd_options);
    // Without this, the image appears off the screen
    $(".openseadragon-container").css("position", "absolute");
/* To change tileSources
	var fluff = [{
        type: 'image',
        url:  'static/content/images/bxa0007.jpg'		
	}];
    viewer.open(fluff);
    $(".openseadragon-container").css("position", "absolute");
*/

	/* Settings */
	$(".fa-cog").click(function() {
		settings = $("#settingsModal").modal();
		c = $("#toolbarDiv").css("z-index");
		settings.css("z-index", c+1);
	});
	/* This is buggy. If you have a tag set to show in critical and switch to diplomatic,
	   you have to change the settings to get the diplomatic styling to work. */
	$("#saveSettings").click(function() {
		showUnclear = $("#showUnclear");
		showAdd = $("#showAdd");
		showDel = $("#showDel");
		settings = [showUnclear, showAdd, showDel];
		switch (true) {
			case $('#currentView').val() == 'diplomatic':
				$.each(settings, function(){
					tag = "tei-" + $(this).attr('id').toLowerCase().replace("show", "")
					if ($(this).prop('checked') == true) {
						$(tag).css("color", "yellow");
					}
					else {
						$(tag).css("color", "black");
					}
				});
			break;
			case $('#currentView').val() == 'proofreading':
				$.each(settings, function(){
					tag = "tei-" + $(this).attr('id').toLowerCase().replace("show", "")
					if ($(this).prop('checked') == true) {
						$(tag).css("color", "yellow");
					}
					else {
						$(tag).css("color", "black");
					}
				});
			break;
			default: // critical
				$.each(settings, function(){
					tag = "tei-" + $(this).attr('id').toLowerCase().replace("show", "")
					if ($(this).prop('checked') == true) {
						$(tag).show();
					}
					else {
						$(tag).hide()
					}
				});
		}
		$(".close").click();
	});
});

/* To do:
1. Figure out how to place marginalia and make them persist across pages.
2. PC handling, other stylistic fine tuning
3. Metadata
4. Handle double <div1>
5. How to do diplomatic/critical views side by side.
*/