async function fetchRecommendation(category) {
    const prompts = {
    seafood: "6월 제철 해산물 요리를 추천해줘",
    vegetable: "6월 제철 야채 요리를 추천해줘",
    fruit: "6월 제철 과일 요리를 추천해줘",
    random: "6월 제철 음식 하나만 추천해줘"
};

    const response = await fetch("https://dev.wenivops.co.kr/services/openai-api", {
    method: "POST",
    headers: {
    "Content-Type": "application/json"
    },
    body: JSON.stringify({
    message: prompts[category],
    system_message: systemPrompt
    })
});

    const result = await response.json();
document.getElementById("foodresult").textContent = result.response;
}

document.getElementById("seafoodbtn").addEventListener("click", () => fetchRecommendation("seafood"));
document.getElementById("vegetablebtn").addEventListener("click", () => fetchRecommendation("vegetable"));
document.getElementById("fruitbtn").addEventListener("click", () => fetchRecommendation("fruit"));
document.getElementById("randombtn").addEventListener("click", () => fetchRecommendation("random"));
