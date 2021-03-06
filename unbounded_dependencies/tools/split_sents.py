import os
def split_results(data_type):
    constructions = ['obj_extract_rel_clause', 'obj_extract_red_rel', 'sbj_extract_rel_clause', 'obj_free_rels', 'obj_qus', 'right_node_raising', 'sbj_embedded']
    features = ['sents', 'predicted_pos', 'predicted_stag', 'predicted_arcs', 'predicted_rels']
    for feature in features:
        with open('{}/{}.txt'.format(feature, data_type)) as f_pred:
            for construction in constructions:
                    if not os.path.isdir('{}/{}'.format(construction, feature)):
                        os.makedirs('{}/{}'.format(construction, feature))
                    with open('longrange-distrib/{}/{}.raw.{}'.format(construction, data_type, construction)) as fin:
                        with open('{}/{}/{}.txt'.format(construction, feature, data_type), 'wt') as fout:
                            for line in fin:
                                fout.write(f_pred.readline())

if __name__ == '__main__':
    split_results('dev')
    split_results('test')
