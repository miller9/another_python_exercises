    function nextLesson() {
    			i=0;
    			myLoop();
    }
     
     
    var i = 0;                    
    var a = document.getElementsByClassName('item-name inline-child caption-text')
    function myLoop () {
    	document.getElementsByClassName('item-name inline-child caption-text')[i].click()          
    	setTimeout(function () {   
    		console.log("8 sec over");
    		var b = document.getElementsByClassName('resource-name body-2-text color-secondary-text')
    		if (b.length!=0){
    			b[0].click()
    			b[1].click()
    		}		
          i++;                    
          if (i < a.length) {           
             myLoop();            
          }
          else{
          	console.log("Lesson Over");
          	var b = document.getElementsByClassName('caption-text color-secondary-text');
    		for(i=0;i<b.length;i++){
    			if(b[i].innerHTML=="Next Lesson"){
    				break;
    			}
    		}
    		if(b[i].innerHTML=="Next Lesson"){
    			b[i].click()
    			setTimeout(nextLesson , 8000);
    		}
    		
          }                       
       }, 8000)
    }
    myLoop();
