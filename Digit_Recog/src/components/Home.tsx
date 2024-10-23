import React, { useState } from "react";

const Home: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [previewImage, setPreviewImage] = useState<string | null>(null);

  const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      const file = event.target.files[0];
      setSelectedFile(file);
      setPreviewImage(URL.createObjectURL(file)); // For image preview
    }
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (selectedFile) {
      const formData = new FormData();
      formData.append("file", selectedFile); // Append the actual File object
      console.log(formData.get("file")); // This will show the file in console
      try {
        const response = await fetch("http://127.0.0.1:8000/predict-digit", {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Prediction result:", data);
      } catch (error) {
        console.error("Error uploading image:", error);
      }
    } else {
      console.log("No image selected");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md max-w-md w-full">
        <h2 className="text-2xl font-bold mb-6 text-center">Upload an Image</h2>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="text-center">
            {previewImage ? (
              <img
                src={previewImage}
                alt="Selected"
                className="mx-auto mb-4 w-48 h-48 object-cover rounded"
              />
            ) : (
              <div className="w-48 h-48 bg-gray-200 mx-auto mb-4 flex items-center justify-center rounded">
                <span className="text-gray-500">No image selected</span>
              </div>
            )}
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Select Image
            </label>
            <input
              type="file"
              accept="image/*"
              onChange={handleImageChange}
              className="mt-2 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div>
          <button
            type="submit"
            className="w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-lg transition duration-300"
          >
            Upload Image
          </button>
        </form>
      </div>
    </div>
  );
};

export default Home;
