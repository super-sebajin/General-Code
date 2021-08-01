
/*
 Author: Sebastian R. Papanikolaou Costa
 Program: GeneralizedGraph.cs
Description: This program is an implmentaion of a generalized,
undirected graph. We will use strings here, but we can generalize,
the labels in the vertices with the 'object'. 
    
 */

using System;
using System.Collections;

namespace Program
{
    class Program
    {
        //Implementation of GraphVertex, holds two constructors
        public class GraphVertex {
            //In the event that no argument is passed to the constuctor, we still
            //count the number of active instances. Invariant: The number of active
            //instances is equal to the number of vertices in the graph.
            private static int instances = 0;
            public string label;
            public ArrayList incidenceList = new ArrayList();

            //Constructor for when no argument is passed
            public GraphVertex() {
                instances++;
            }

            //Constructor to initialize the
            public GraphVertex(string value) {

                instances++;
                label = value;
            }

            //getter property for instances
            public static int Instances {
                get { return instances; }

            }
            ~GraphVertex() {

                instances--;
            }

        }


        public class GraphEdge {

            private static int instances = 0;
            public GraphVertex[] vertices;

            //Constructor
            public GraphEdge(GraphVertex vertexA, GraphVertex vertexB) {
                instances++;
                vertices = new GraphVertex[2] {vertexA, vertexB};
                UpdateVertices();
            }

            private void UpdateVertices() {
                foreach (GraphVertex v in this.vertices) {
                    v.incidenceList.Add(this);
                }
            }

            //getter property for instances
            public static int Instances {
                get { return instances; }
            }

            ~GraphEdge() {
                instances--;

            }

        }


        public class Graph {
            private ArrayList vertexSet;
            private ArrayList edgeSet;
            private bool isEmpty;

            //Represents an empty Graph
            public Graph() {
                isEmpty = true;
            }

            //Represents a single vertex graph
            public Graph(GraphVertex vertex) {
                vertexSet.Add(vertex);
            }

            //Represents a two vertex simple graph
            public Graph(GraphVertex vertexA, GraphVertex vertexB) {
                GraphEdge edge = new GraphEdge(vertexA, vertexB);
                vertexSet.Add(vertexA);
                vertexSet.Add(vertexB);
                edgeSet.Add(edge);
            }

        }

        static void Main(string[] args)
        {
            GraphVertex testVertex1 = new GraphVertex();
            GraphVertex testVertex2 = new GraphVertex();

            Console.WriteLine("There is {0} instance of class GraphVertex active.", GraphVertex.Instances);


            GraphEdge testEdge = new GraphEdge(testVertex1, testVertex2);

            Console.WriteLine("There is {0} instance of class GraphEdge active.", GraphEdge.Instances);
        }
    }
}
