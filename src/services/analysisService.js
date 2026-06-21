//const API_URL = "http://127.0.0.1:5000";
 const API_URL = "https://trustshield-backend-production.up.railway.app/"
export async function analyzeText(message) {

    const response = await fetch(
        `${API_URL}/analyze`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify({
                message
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.error ||
            "Analysis failed."
        );
    }

    return data;
}

export async function analyzeImage(imageFile) {

    const formData = new FormData();

    formData.append(
        "image",
        imageFile
    );

    const response = await fetch(
        `${API_URL}/analyze-image`,
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.error ||
            "Image analysis failed."
        );
    }

    return data;
}