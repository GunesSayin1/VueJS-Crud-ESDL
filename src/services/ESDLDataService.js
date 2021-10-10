import http from "../http-common";

class esdlDataService {
    getAll() {
        return http.get("/esdls");
    }

    get(id) {
        return http.get(`/esdls/${id}`);
    }

    create(data) {
        return http.post("/esdls", data);
    }

    update(id, data) {
        return http.put(`/esdls/${id}`, data);
    }

    delete(id) {
        return http.delete(`/esdls/${id}`);
    }

    deleteAll() {
        return http.delete(`/esdls`);
    }

    findByTitle(title) {
        return http.get(`/esdls?title=${title}`);
    }
}

export default new esdlDataService();