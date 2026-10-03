
async function askQuestion(){

    
    const query=document.getElementById("query").value;


    const answediv=document.getElementById("answer");
    const sourcesdiv=document.getElementById("sources");


    if (!query.trim()){
        answediv.textContent="Please Enter the question..!";
        sourcesdiv.innerHTML="";
        return;
    }
    

    answediv.textContent="Searching Documents and Getting Answers.......";
    sourcesdiv.innerHTML="";

    const button=document.querySelector("button");
    button.disabled=true;
    button.textContent="Searching...";

    const sourcecount=document.getElementById("source_count");
    sourcecount.textContent="";


    try{

        const response= await fetch("/ask",{

            method: "POST",

            headers: {
                "Content-Type":"application/json"
            },
        
            body: JSON.stringify({
                query : query
            })
            });



        if (!response.ok){
            throw new Error("Server Error");
        }



        const data = await response.json();

        sourcecount.textContent=`(${data.sources.length})`;
         
        // console.log(data);

        answediv.textContent  =  data.answer || "No Relevant Information Found";


        if (data.sources.length===0) {
            sourcesdiv.textContent="No Relevant Information Found..!"
        }

        for (const source of data.sources){

            const sourcediv=document.createElement("div");
            sourcediv.className="source";


            const sourcetitle=document.createElement("p")
            sourcetitle.textContent=`Source: [${source[0]}] ${source[1]}`

            const chunk=document.createElement("p")
            chunk.textContent=`Chunk: ${source[2]}`

            const Similarity_score=document.createElement("p")
            Similarity_score.textContent=`Similarity: ${(source[3]*100).toFixed(2)}%`

            const Rerank_score=document.createElement("p")
            Rerank_score.textContent=`Rerank:  ${(source[4]).toFixed(2)}`

            const Retrieved_text=document.createElement("p")
            Retrieved_text.textContent=`Retrieved Text:  ${source[5]}`

            sourcediv.append(
                sourcetitle,
                chunk,
                Similarity_score,
                Rerank_score,
                Retrieved_text
            )

            sourcesdiv.appendChild(sourcediv);
        }

    }catch (error){
        answediv.textContent="Something went Wrong...!";
        console.error(error);

    } finally{

        button.disabled=false;
        button.textContent="Ask";

    }
    
}


document.getElementById("query").addEventListener("keydown", function(event){
    
    if (event.key=="Enter"){
        askQuestion();
    }
});


function clearsearch(){

    document.getElementById("query").value="";
    document.getElementById("answer").textContent="";
    document.getElementById("sources").innerHTML="";
    document.getElementById("source_count").textContent="";
    

}




document.getElementById("upload_form").addEventListener("submit",async function(event){

    event.preventDefault();

    const fileinput=document.getElementById("documents")
    const status=document.getElementById("upload_status")

    const files=fileinput.files


    if(files.length===0){
        status.textContent="Please Select At least One Document .. !"
        return;
    }

    for(const file of files ){
        if(!file.name.toLowerCase().endsWith(".txt")){
            status.textContent="Only .txt files are allowed.. !"
            return;
        }
    }

    const formdata= new FormData()

    for (const file of files){
        formdata.append("documents",file)
    }

    status.textContent=`Uploading ${files.length} Documents`

    try{
        const response = await fetch("/upload",
            {
                method:"POST",
                body: formdata
            }
        );

        const data= await response.json();

        if(!response.ok){
            throw new Error(data.error || "Upload Failed");
        }

        status.textContent=data.message;

        fileinput.value=""

        loaddocuments();

    }catch(error){
        status.textContent=error.message;

    }

    


});



async function loaddocuments() {

    const documentslist=document.getElementById("documents_list");

    try{
        const response = await fetch("/documents");

        if (!response.ok){
            throw new Error("Failed to load Documents");
        };

        const data=await response.json();

        documentslist.innerHTML="";

        if (data.documents.length === 0){
            documentslist.textContent="No documents uploaded";
            return ;
        }

        documentslist.textContent=data.documents.join("\n");


    }catch(error){

        documentslist.textContent="Could not load Documents..!";
        console.error(error);

    };
    
};

loaddocuments();