#include "stdafx.h"
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const long long INF = 2000000000;

struct Edge {
	int from, to, capacity, flow, index;
	Edge(int from, int to, int cap, int flow, int index) :
		from(from), to(to), capacity(cap), flow(flow), index(index) {}
};

struct Dinitz {
	int vertices;
	vector<vector<Edge> > edges;
	vector<Edge *> G;
	vector<int> F;

	Dinitz(int N) : vertices(N), edges(N), G(N), F(N) {}

	void AddingEdge(int from, int to, int cap) {
		edges[from].push_back(Edge(from, to, cap, 0, edges[to].size()));
		if (from == to) edges[from].back().index++;
		edges[to].push_back(Edge(to, from, 0, 0, edges[from].size() - 1));
	}
	
	long long BlockFlow(int s, int t) {
		fill(G.begin(), G.end(), (Edge *)NULL);
		G[s] = &edges[0][0] - 1;

		int head = 0, tail = 0;
		F[tail++] = s;
		while (head < tail) {
			int x = F[head++];
			for (int i = 0; i < edges[x].size(); i++) {
				Edge &e = edges[x][i];
				if (!G[e.to] && e.capacity - e.flow > 0) {
					G[e.to] = &edges[x][i];
					F[tail++] = e.to;
				}
			}
		}
		if (!G[t]) return 0;

		long long ret = 0;
		for (int i = 0; i < edges[t].size(); i++) {
			Edge *start = &edges[edges[t][i].to][edges[t][i].index];
			int x = INF;
			for (Edge *e = start; x && e != G[s]; e = G[e->from]) {
				if (!e) { x = 0; break; }
				x = min(x, e->capacity - e->flow);
			}
			if (x == 0) continue;
			for (Edge *e = start; x && e != G[s]; e = G[e->from]) {
				e->flow += x;
				edges[e->to][e->index].flow -= x;
			}
			ret += x;
		}
		return ret;
	}
	long long GetMaxFlow(int s, int t) {
		long long ret = 0;
		while (long long flow = BlockFlow(s, t))
			ret += flow;
		return ret;
	}

	
};
int main() {
	int N, M; scanf("%d %d", &N, &M);
	Dinitz D(N);
	while (M--) {
		int A, B, C;
		scanf("%d %d %d", &A, &B, &C);
		D.AddingEdge(A - 1, B - 1, C);
		D.AddingEdge(B - 1, A - 1, C);
	}
	printf("%lld\n", D.GetMaxFlow(0, N - 1));
	return 0;
}
