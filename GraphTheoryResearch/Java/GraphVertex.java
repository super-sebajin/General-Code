//Author: Sebastian R. Papanikolaou Costa
//Java implentation of the class "Graph Vertex" in UnidrectedGraph.py
//Due to Java being strongly typed, this implementation will work with string data.

package GeneralCode.GraphTheoryResearch.Java;
import java.util.ArrayList;


public class GraphVertex{


    //Vertex will hold the data, degree and an incidence list in the form of an array
    class Vertex{
        String data;
        int degree;
        ArrayList<GraphEdge.Edge> incidenceList = new ArrayList<GraphEdge.Edge>();

        public Vertex(String value){
            this.data = new String(value);
        }
        
    }
}