const systemPrompt = "당신은 음식 추천 전문가입니다. 계절에 맞는 요리를 간단하고 이해하기 쉽게 추천해주세요.";

async function fetchRecommendation(category) {
    const prompts = {
        seafood: "6월 제철 해산물 요리를 추천해줘",
        vegetable: "6월 제철 야채 요리를 추천해줘",
        fruit: "6월 제철 과일 요리를 추천해줘",
        random: "6월 제철 음식 하나만 추천해줘"
    };

    try {
        const response = await fetch("https://dev.wenivops.co.kr/services/openai-api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify([
                { role: "system", content: systemPrompt },
                { role: "user", content: prompts[category] }
            ])
        });

        const result = await response.json();
        console.log("🟢 응답 전체:", JSON.stringify(result, null, 2)); // 디버깅용 콘솔 출력

        const foodResultElement = document.getElementById("foodresult");
        const content = result.choices?.[0]?.message?.content;

        if (content) {
            const lines = content.split("\n").filter(line => line.trim() !== "");
            if (lines.length > 1) {
                foodResultElement.innerHTML = "<ul>" + lines.map(line => `<li>${line}</li>`).join("") + "</ul>";
            } else {
                foodResultElement.textContent = content;
            }
        } else {
            foodResultElement.textContent = "추천 결과가 없습니다. (응답 없음)";
        }

    } catch (error) {
        console.error("❌ 추천 요청 실패:", error);
        document.getElementById("foodresult").textContent = "추천을 가져오는데 실패했습니다.";
    }
}

document.getElementById("seafoodbtn").addEventListener("click", () => fetchRecommendation("seafood"));
document.getElementById("vegetablebtn").addEventListener("click", () => fetchRecommendation("vegetable"));
document.getElementById("fruitbtn").addEventListener("click", () => fetchRecommendation("fruit"));
document.getElementById("randombtn").addEventListener("click", () => fetchRecommendation("random"));
