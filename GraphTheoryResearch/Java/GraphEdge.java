//Author: Sebastian R. Papanikolaou Costa

package GeneralCode.GraphTheoryResearch.Java;


public class GraphEdge {
    //Edge will have the exact same behaivor as a doubly linked list node, with out the data
    class Edge {
        GraphVertex.Vertex vertexA;
        GraphVertex.Vertex vertexB;
        public Edge(GraphVertex.Vertex vA, GraphVertex.Vertex vB ){
            vertexA = vA;
            vertexB = vB;
            updateIncidenceLists();
        }
        private void updateIncidenceLists(){
            vertexA.incidenceList.add(this);
            vertexB.incidenceList.add(this);
        }
    } 
    public static void main(String[] args){
        //Testing Area
        //Verify correct initialization of Edge
        System.out.println("Testing - Edge initializaton: ");
        GraphVertex.Vertex testA = new GraphVertex().new Vertex("100");
        GraphVertex.Vertex testB = new GraphVertex().new Vertex("001");
        GraphEdge.Edge testEdge = new GraphEdge().new Edge(testA, testB);

        System.out.println("Verififying the initialization of testEdge");
        System.out.println("Internal vertexA.data: " + testEdge.vertexA.data);
        System.out.println("Internal vertexB.data: " + testEdge.vertexB.data);
      
        System.out.println("Verififying the initialization of testA and testB"); 
        System.out.println("testA.data: " + testA.incidenceList.get(0).vertexA.data);
        System.out.println("testB.data: " + testA.incidenceList.get(0).vertexB.data);
        System.out.println("testEdge has initialized without error!");

  
    }
}