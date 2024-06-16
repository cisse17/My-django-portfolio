document.addEventListener("DOMContentLoaded", function(){
    const nameSearch = document.getElementById("name-search")
    const tags = document.querySelectorAll(".tag")
    const projets = document.querySelectorAll(".projet")


    function filterProjets(){
        const nameQuery = nameSearch.value.toLowerCase();

        projets.forEach((projet) => {
            const name = projet.getAttribute("data-name")
            const nameMatch = name.includes(nameQuery)

            if (nameMatch){
                projet.style.display = "";
            } else {
                projet.style.display = "none";
            }
        })
    }


    tags.forEach((tag) => {
        tag.addEventListener("click", function(){
            const selectedTag = this.getAttribute("data-tag")

            projets.forEach((projet) => {
                const projetTag = projet.getAttribute("data-tags")

                if (projetTag.includes(selectedTag)){
                    projet.style.display = "";
                }else{
                    projet.style.display = "none";
                }
            })
        })
    })

    nameSearch.addEventListener("keyup", filterProjets)
})