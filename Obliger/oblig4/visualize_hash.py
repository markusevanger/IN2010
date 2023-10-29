from graphviz import Digraph


def create_hash_viz(hashset):

    # Create a Digraph
    dot = Digraph(comment='Hashset Visualization', engine="osage")


    # Create a list to store the calculated values
    values = []

    # Kalkulere farge basert på subliste
    max_length = max(len(lst) if lst is not None else 0 for lst in hashset)
    
    for lst in hashset:
        if lst is not None:
            value = len(lst) / max_length
            values.append(value)
        else:
            values.append(None)

    # Set up node attributes
    dot.attr(label=f"Høyeste antall kollisjoner: {max_length}")
    for i, sublist in enumerate(hashset):
        if sublist is not None:
            size = len(sublist)
            opacity = 1-(size / len(hashset))
            dot.node(str(i), label=f'{len(sublist)}', shape='ellipse', style='filled', fillcolor=f"0.5 1 {values[i]}")
        else: 
            dot.node(str(i), label=f'{0}', shape='ellipse', style='filled', fillcolor=f"0 0 100" )

    

    # Save the DOT file
    dot_file_path = 'hashset_visualization.dot'
    dot.render(dot_file_path, format='png', cleanup=True, view=True)

    print(f"DOT file saved as {dot_file_path}.")
