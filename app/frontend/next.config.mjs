/** @type {import('next').NextConfig} */
const API_URL = process.env.API_URL || "http://localhost:8000";

const nextConfig = {
  // Proxy /api/* to the FastAPI backend so the browser fetches same-origin (no CORS).
  async rewrites() {
    return [{ source: "/api/:path*", destination: `${API_URL}/api/:path*` }];
  },
};

export default nextConfig;
