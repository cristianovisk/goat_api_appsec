import uvicorn
import goat

if __name__ == "__main__":
    uvicorn.run("goat:app", host='0.0.0.0', port=8080, log_level="info", timeout_keep_alive=500, timeout_graceful_shutdown=500, ws_ping_timeout=500)