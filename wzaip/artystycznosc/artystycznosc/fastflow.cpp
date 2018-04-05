#include "stdafx.h"
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const long long INF = 2345678901;

struct Edge {
	int from, to, capacity, flow, index;
	Edge(int from, int to, int cap, int flow, int index) :
		from(from), to(to), capacity(cap), flow(flow), index(index) {}
};

struct Dinic {
	int vertices;
	vector<vector<Edge> > edges;
	vector<Edge *> dad;
	vector<int> Q;

	Dinic(int N) : vertices(N), edges(N), dad(N), Q(N) {}

	void AddEdge(int from, int to, int cap) {
		edges[from].push_back(Edge(from, to, cap, 0, edges[to].size()));
		if (from == to) edges[from].back().index++;
		edges[to].push_back(Edge(to, from, 0, 0, edges[from].size() - 1));
	}

	long long BlockingFlow(int s, int t) {
		fill(dad.begin(), dad.end(), (Edge *)NULL);
		dad[s] = &edges[0][0] - 1;

		int head = 0, tail = 0;
		Q[tail++] = s;
		while (head < tail) {
			int x = Q[head++];
			for (int i = 0; i < edges[x].size(); i++) {
				Edge &e = edges[x][i];
				if (!dad[e.to] && e.capacity - e.flow > 0) {
					dad[e.to] = &edges[x][i];
					Q[tail++] = e.to;
				}
			}
		}
		if (!dad[t]) return 0;

		long long totflow = 0;
		for (int i = 0; i < edges[t].size(); i++) {
			Edge *start = &edges[edges[t][i].to][edges[t][i].index];
			int amt = INF;
			for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
				if (!e) { amt = 0; break; }
				amt = min(amt, e->capacity - e->flow);
			}
			if (amt == 0) continue;
			for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
				e->flow += amt;
				edges[e->to][e->index].flow -= amt;
			}
			totflow += amt;
		}
		return totflow;
	}


	long long GetMaxFlow(int s, int t) {
		long long totflow = 0;
		while (long long flow = BlockingFlow(s, t))
			totflow += flow;
		return totflow;
	}
};
int main() {
	int N, M; scanf("%d %d", &N, &M);
	Dinic D(N);
	while (M--) {
		int A, B, C;
		scanf("%d %d %d", &A, &B, &C);
		D.AddEdge(A - 1, B - 1, C);
		D.AddEdge(B - 1, A - 1, C);
	}
	printf("%lld\n", D.GetMaxFlow(0, N - 1));
	return 0;
}
