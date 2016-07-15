$(function() {

  // We can attach the `fileselect` event to all file inputs on the page
  $(document).on('change', ':file', function() {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
  });

  // We can watch for our custom `fileselect` event like this
  $(document).ready( function() {
      $(':file').on('fileselect', function(event, numFiles, label) {

          var input = $(this).parents('.input-group').find(':file'),
          	  text = $('#file_name'),	
              log = numFiles > 1 ? numFiles + ' files selected' : label;
              
          if( input.length ) {
              text.text(log);
          } else {
              if( log ) alert(log);
          }

      });
  });
  
});