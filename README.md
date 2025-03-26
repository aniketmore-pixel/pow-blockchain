# pow-blockchain
A simple Python-based blockchain implementation with proof-of-work mining and chain validation. 🚀

## **Prerequisites**  
- Install [Docker](https://docs.docker.com/get-docker/)  

## **Setup and Run**  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/your-repo/blockforge.git
   cd blockforge
   ```

2. **Build the Docker image:**  
   ```sh
   docker build -t blockforge .
   ```

3. **Run the blockchain script inside a container:**  
   ```sh
   docker run --rm blockforge
   ```

## **Project Structure**  
- 📜 **pow-blockchain.py** - Core blockchain logic  
- 🛠 **Dockerfile** - Defines the environment to run the script  

## **Notes**  
- The script executes, mines blocks, and exits after displaying blockchain details.  
- Modify `pow-blockchain.py` to add transactions or adjust mining difficulty.  

